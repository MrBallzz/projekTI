import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Ensiklopedia Tahu", page_icon="🍲", layout="centered")

# --- CSS Custom agar lebih rapi ---
st.markdown("""
    <style>
    .main {
        background-color: #fcf8f0;
    }
    h1 {
        color: #d35400;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Menu ---
st.sidebar.title("🍱 Menu Navigasi")
menu = st.sidebar.radio("Pilih Topik:", ["Sejarah Tahu", "Kandungan & Manfaat", "Cara Pembuatan", "5 Resep Sederhana"])

# --- Konten Utama ---
st.title("🍲 Dunia Tahu")
st.write("Selamat datang di panduan lengkap tentang Tahu, makanan kaya protein yang melegenda.")
st.divider()

if menu == "Sejarah Tahu":
    st.header("⏳ Sejarah Tahu")
    st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800", caption="Tahu dalam berbagai sajian.")
    st.markdown("""
    Tahu berasal dari **Tiongkok**, tepatnya pada masa Dinasti Han sekitar 2.000 tahun yang lalu. 
    Menurut legenda, tahu ditemukan oleh **Pangeran Liu An**.
    
    Tahu kemudian menyebar ke seluruh Asia, termasuk Jepang (disebut *Tofu*) dan Indonesia, 
    di mana tahu telah menjadi bagian tak terpisahkan dari budaya kuliner masyarakat lokal.
    """)

elif menu == "Kandungan & Manfaat":
    st.header("💪 Kandungan & Manfaat")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Nutrisi (per 100g)")
        st.write("- Protein: 8-10g")
        st.write("- Lemak: 4-5g")
        st.write("- Kalori: 76 kkal")
        st.write("- Kalsium & Zat Besi")
        
    with col2:
        st.subheader("Manfaat Kesehatan")
        st.success("Menurunkan kolesterol jahat (LDL).")
        st.success("Mencegah pengeroposan tulang.")
        st.success("Membantu fungsi otak dan elastisitas kulit.")

elif menu == "Cara Pembuatan":
    st.header("⚙️ Proses Pembuatan")
    st.info("Berikut adalah langkah-langkah tradisional mengubah kedelai menjadi tahu:")
    steps = [
        "**Perendaman:** Kedelai direndam hingga mengembang.",
        "**Penggilingan:** Kedelai digiling dengan air menjadi susu kedelai kasar.",
        "**Perebusan:** Susu kedelai direbus hingga mendidih.",
        "**Penyaringan:** Memisahkan sari kedelai dari ampasnya (okara).",
        "**Penggumpalan:** Sari kedelai dicampur koagulan (asam/cuka) hingga menggumpal.",
        "**Pencetakan:** Gumpalan tahu dipres untuk mengeluarkan air hingga padat."
    ]
    for i, step in enumerate(steps, 1):
        st.write(f"{i}. {step}")

elif menu == "5 Resep Sederhana":
    st.header("🍳 Resep Masakan Tahu")
    
    resep = {
        "Tahu Goreng Krispi": "Potong tahu kotak-kotak, balur tepung bumbu kering, goreng hingga kecokelatan.",
        "Tahu Bacem": "Ungkep tahu dengan air kelapa, gula jawa, ketumbar, dan bawang hingga meresap, lalu goreng sebentar.",
        "Pepes Tahu": "Hancurkan tahu, campur dengan telur, kemangi, dan bumbu halus. Kukus dalam daun pisang.",
        "Tahu Gejrot": "Potong tahu pong, siram dengan kuah asam jawa dan ulekan bawang putih serta cabai rawit.",
        "Tumis Tahu Tauge": "Tumis bawang merah-putih, masukkan potongan tahu sutra dan tauge segar. Beri kecap asin dan garam."
    }
    
    for nama, cara in resep.items():
        with st.expander(f"📖 {nama}"):
            st.write(f"**Cara Membuat:** {cara}")

# --- Footer ---
st.divider()
st.caption("Dibuat dengan Python & Streamlit")