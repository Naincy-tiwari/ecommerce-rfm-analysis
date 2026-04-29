
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="E-Commerce RFM Dashboard",
    page_icon="🛒",
    layout="wide"
)

@st.cache_data
def load_data():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df  = pd.read_csv(
        os.path.join(base, 'data', 'processed', 'clean_retail.csv'),
        parse_dates=['InvoiceDate']
    )
    rfm = pd.read_csv(
        os.path.join(base, 'data', 'processed', 'rfm_segments.csv')
    )
    return df, rfm

df, rfm = load_data()

# ── Sidebar ───────────────────────────────────
st.sidebar.title("🛒 RFM Dashboard")
st.sidebar.markdown("**E-Commerce Sales Analysis**")
st.sidebar.markdown("---")

all_segments = ['All'] + sorted(rfm['Segment'].unique().tolist())
selected_seg = st.sidebar.selectbox("Filter by Segment", all_segments)
rfm_filtered = rfm if selected_seg == 'All' \
               else rfm[rfm['Segment'] == selected_seg]

# ── Header ────────────────────────────────────
st.title("🛒 E-Commerce Sales & RFM Dashboard")
st.markdown("*Customer behavior, revenue trends and RFM segmentation*")
st.markdown("---")

# ── KPI Cards ─────────────────────────────────
st.subheader("📊 Key Business Metrics")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("💰 Total Revenue",
          f"£{df['Revenue'].sum()/1e6:.2f}M")
c2.metric("👥 Customers",
          f"{df['Customer ID'].nunique():,}")
c3.metric("📦 Total Orders",
          f"{df['Invoice'].nunique():,}")
c4.metric("🛍️ Avg Order Value",
          f"£{df.groupby('Invoice')['Revenue'].sum().mean():.0f}")
c5.metric("🏆 Champions",
          f"{(rfm['Segment']=='Champions').sum():,}",
          f"{(rfm['Segment']=='Champions').sum()/len(rfm)*100:.1f}% of base")

st.markdown("---")

# ── Revenue Trend + Donut ─────────────────────
col_left, col_right = st.columns([3, 2])

with col_left:
    st.subheader("📈 Monthly Revenue Trend")
    monthly = (
        df.groupby(df['InvoiceDate'].dt.to_period('M'))['Revenue']
        .sum().reset_index()
    )
    monthly['InvoiceDate'] = monthly['InvoiceDate'].astype(str)
    fig_trend = px.area(
        monthly, x='InvoiceDate', y='Revenue',
        color_discrete_sequence=['#1f77b4'],
        labels={'Revenue':'Revenue (£)','InvoiceDate':'Month'}
    )
    fig_trend.update_layout(
        showlegend=False,
        yaxis_tickprefix='£',
        yaxis_tickformat=',.0f',
        margin=dict(l=0,r=0,t=10,b=0)
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col_right:
    st.subheader("🍩 Revenue by Segment")
    seg_rev = (
        rfm.groupby('Segment')['Monetary'].sum()
        .reset_index().sort_values('Monetary', ascending=False)
    )
    fig_donut = px.pie(
        seg_rev, values='Monetary', names='Segment',
        hole=0.55,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_donut.update_layout(margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_donut, use_container_width=True)

st.markdown("---")

# ── Heatmap + Segment Bar ─────────────────────
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("🔥 RFM Heatmap")
    pivot = rfm.pivot_table(
        index='R_Score', columns='F_Score',
        values='Monetary', aggfunc='mean'
    ).round(0)
    fig_heat = px.imshow(
        pivot, color_continuous_scale='YlOrRd',
        labels=dict(x="Frequency Score",
                    y="Recency Score",
                    color="Avg Revenue £"),
        text_auto=True, aspect='auto'
    )
    fig_heat.update_layout(margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_heat, use_container_width=True)

with col_r:
    st.subheader("👥 Customers per Segment")
    seg_count = (rfm_filtered['Segment']
                 .value_counts().reset_index())
    seg_count.columns = ['Segment', 'Count']
    fig_bar = px.bar(
        seg_count.sort_values('Count'),
        x='Count', y='Segment', orientation='h',
        color='Count', color_continuous_scale='Blues',
        text='Count'
    )
    fig_bar.update_layout(
        showlegend=False,
        coloraxis_showscale=False,
        margin=dict(l=0,r=0,t=10,b=0)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# ── Top Products + Countries ──────────────────
col_p, col_c = st.columns(2)

with col_p:
    st.subheader("🏆 Top 10 Products")
    top_prod = (
        df.groupby('Description')['Revenue'].sum()
        .nlargest(10).reset_index().sort_values('Revenue')
    )
    fig_prod = px.bar(
        top_prod, x='Revenue', y='Description',
        orientation='h',
        color_discrete_sequence=['#2ecc71'],
        text=top_prod['Revenue'].apply(lambda x: f'£{x:,.0f}')
    )
    fig_prod.update_layout(
        margin=dict(l=0,r=0,t=10,b=0),
        yaxis_title=''
    )
    st.plotly_chart(fig_prod, use_container_width=True)

with col_c:
    st.subheader("🌍 Revenue by Country (excl. UK)")
    top_country = (
        df[df['Country'] != 'United Kingdom']
        .groupby('Country')['Revenue'].sum()
        .nlargest(10).reset_index().sort_values('Revenue')
    )
    fig_country = px.bar(
        top_country, x='Revenue', y='Country',
        orientation='h',
        color_discrete_sequence=['#e74c3c'],
        text=top_country['Revenue'].apply(lambda x: f'£{x:,.0f}')
    )
    fig_country.update_layout(
        margin=dict(l=0,r=0,t=10,b=0),
        yaxis_title=''
    )
    st.plotly_chart(fig_country, use_container_width=True)

st.markdown("---")

# ── RFM Table ─────────────────────────────────
st.subheader("📋 RFM Segment Detail Table")
display_cols = ['Customer ID','Recency','Frequency','Monetary',
                'R_Score','F_Score','M_Score','RFM_Total','Segment']
st.dataframe(
    rfm_filtered[display_cols]
    .sort_values('RFM_Total', ascending=False)
    .reset_index(drop=True),
    use_container_width=True,
    height=300
)
csv = rfm_filtered.to_csv(index=False)
st.download_button(
    "⬇️ Download RFM Data",
    csv, 'rfm_segments.csv', 'text/csv'
)
