import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
from streamlit_option_menu import option_menu

# Sayfa yapılandırması
st.set_page_config(page_title="DBYS DIM Dashboard", layout="wide")
st.title("📊 DBYS DIM Detailed Dashboard")

# Responsive padding ayarı
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .main .block-container {
        padding: 1.5rem 2.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔸 Modern Sidebar Menü
with st.sidebar:
    st.markdown("### 🧭 Navigasyon", unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=[
            "📄 Ana Sayfa",
            "🔧 Donanımsal Arıza",
            "📦 Doluluk Durumları",
            "💳 Ödeme Hataları",
            "♻️ İade Farklılıkları"
        ],
        default_index=0,
        menu_icon=None,       # Sağdaki ekstra ikonları kapatmak için
    )

# 🔍 Sayfa içeriği yönlendirme
page = selected.replace("📄 ", "").replace("🔧 ", "").replace("📦 ", "").replace("💳 ", "").replace("♻️ ", "")

# 🏠 Ana Sayfa
if page == "Ana Sayfa":
    st.success("Sol menüden panel seçerek sistem verilerini grafiklerle görüntüleyebilirsiniz.")

# 🔧 Donanımsal Arıza Özet
elif page == "Donanımsal Arıza":
    st.subheader("🔧 DIM Donanımsal Arıza Özet")

    data = pd.DataFrame({
        "DIM DB Serial Number": [f"DB{100+i}" for i in range(10)],
        "Alarm Type": np.random.choice(["Emergency", "Sensor", "Compactor"], 10),
        "Alarm Descriptions": np.random.choice([
            "Emergency circuit broken", "Compactor alarm",
            "Bin #2 is full", "Conveyor problem"
        ], 10),
        "Last Seen": [datetime.now() - timedelta(minutes=np.random.randint(1, 60)) for _ in range(10)]
    })

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(data, x="Alarm Type", color="Alarm Type", title="Alarm Tipi Dağılımı", text_auto=True)
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.histogram(data, x="Alarm Descriptions", color="Alarm Descriptions",
                            title="Alarm Açıklama Dağılımı", text_auto=True)
        st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(data)

# ♻️ Doluluk Durumları
elif page == "Doluluk Durumları":
    st.subheader("📦 DIM Doluluk Durumları")

    data = pd.DataFrame({
        "İstasyon": [f"İstasyon-{i}" for i in range(1, 6)],
        "PET": np.random.randint(60, 100, 5),
        "ALUMINYUM": np.random.randint(60, 100, 5),
        "CAM": np.random.randint(60, 100, 5)
    })

    fig = px.bar(data, x="İstasyon", y=["PET", "ALUMINYUM", "CAM"],
                 barmode="group", title="Doluluk Oranları", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(data)

# 💳 Ödeme Hataları
elif page == "Ödeme Hataları":
    st.subheader("💳 DIM Ödeme Hataları")

    data = pd.DataFrame({
        "Transaction Id": [f"T{i}" for i in range(10)],
        "Deposit Point Id": np.random.randint(1000, 1010, 10),
        "Transaction Date": [datetime.now() - timedelta(days=np.random.randint(1, 15)) for _ in range(10)],
        "Payment Response": np.random.choice(["ERROR", "TIMEOUT", "DECLINED"], 10),
        "Item Count": np.random.randint(1, 6, 10)
    })

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.pie(data, names="Payment Response", title="Ödeme Hataları Dağılımı")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.bar(data, x="Transaction Id", y="Item Count", color="Payment Response",
                      title="İşlem Bazlı Öğeler ve Hatalar", text_auto=True)
        st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(data)

# 🔁 İade Farklılıkları
elif page == "İade Farklılıkları":
    st.subheader("♻️ İade İşlem Adet Farklılıkları")

    data = pd.DataFrame({
        "UserSessionID": [f"UID{i}" for i in range(5)],
        "İşlemTarihi": pd.date_range(end=datetime.now(), periods=5),
        "TransactionAmbalajSayısı": [3, 4, 5, 6, 7],
        "AcceptPackageIadeSayısı": [3, 2, 5, 5, 6]
    })

    data["Fark"] = data["TransactionAmbalajSayısı"] - data["AcceptPackageIadeSayısı"]

    fig = px.bar(data, x="UserSessionID", y="Fark", color="Fark",
                 title="İade Sayı Farklılıkları", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(data)
