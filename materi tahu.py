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
    .stExpander {
        background-color: #ffffff;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Menu ---
st.sidebar.title("🍱 Menu Navigasi")
menu = st.sidebar.radio("Pilih Topik:", [
    "Sejarah Tahu", 
    "Kandungan & Manfaat", 
    "Cara Pembuatan", 
    "5 Resep Sederhana",
    "Cara Menyimpan Tahu"
])

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

elif menu == "Resep Sederhana":
    st.header("🍳 Resep Masakan Tahu")
    st.write("Klik pada judul resep untuk melihat bahan, langkah, dan video tutorialnya.")

    # Resep 1: Tahu Cabai Garam
    with st.expander("🌶️ Tahu Cabai Garam"):
        st.write("**Deskripsi:** Menu favorit Chinese food yang krispi dan gurih.")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Bahan:**\n- 1 blok tahu putih\n- 3 sdm maizena\n- 5 siung baput\n- 10 cabai rawit\n- Daun bawang\n- Garam & kaldu")
        with col2:
            st.markdown("**Langkah:**\n1. Balur tahu dengan maizena.\n2. Goreng hingga garing.\n3. Tumis bumbu hingga harum.\n4. Masukkan tahu, aduk rata.")
        st.link_button("📺 Tonton Tutorial di YouTube", "https://youtu.be/y6eRAgaqi7I?si=V-EUpYVfR-Rf8rxq")

    # Resep 2: Semur Tahu Kentang
    with st.expander("🍯 Semur Tahu Kentang"):
        st.write("**Deskripsi:** Rasa manis gurih yang cocok untuk anak-anak.")
        st.markdown("""
        **Bahan:** 5 tahu (goreng setengah matang), 2 kentang (goreng), 5 sdm kecap manis, salam, serai.
        **Bumbu Halus:** Bawang merah/putih, kemiri, merica.
        
        **Langkah:**
        1. Tumis bumbu halus & rempah daun.
        2. Masukkan tahu & kentang.
        3. Tambahkan kecap dan air (300ml).
        4. Masak hingga meresap.
        """)
        st.link_button("📺 Tonton Tutorial di YouTube", "https://youtu.be/borc_QEvzLw?si=WPVKwgn8qJNOug-x")

    # Resep 3: Tahu Telur Jatim
    with st.expander("🥜 Tahu Telur Khas Jawa Timur"):
        st.write("**Deskripsi:** Hidangan protein tinggi dengan saus kacang segar.")
        st.markdown("""
        **Bahan:** 2 tahu putih, 2 telur, tauge.
        **Saus:** 50g kacang goreng, baput, cabai, kecap manis, petis (opsional).
        
        **Langkah:**
        1. Kocok telur & tahu, goreng dadu tebal.
        2. Ulek bumbu saus hingga kekentalan pas.
        3. Tata telur tahu & tauge, siram saus.
        """)
        st.link_button("📺 Tonton Tutorial di YouTube", "https://youtu.be/3sxYn_zKivw?si=cu3jQEeTDC4oBD8W")

    # Resep 4: Pepes Tahu Kemangi
    with st.expander("🍃 Pepes Tahu Kemangi"):
        st.write("**Deskripsi:** Opsi sehat tanpa minyak goreng.")
        st.markdown("""
        **Bahan:** 5 tahu (hancurkan), kemangi, 1 telur, daun pisang.
        **Bumbu Halus:** Bawang merah/putih, kemiri, cabai merah, gula garam.
        
        **Langkah:**
        1. Campur tahu, bumbu, telur, & kemangi.
        2. Bungkus dengan daun pisang.
        3. Kukus 20-25 menit.
        """)
        st.link_button("📺 Tonton Tutorial di YouTube", "https://youtu.be/5sXx5xVf_p0?si=0OoFracT4y54dv7L")

    # Resep 5: Tahu Mapo
    with st.expander("🏮 Tahu Mapo (Mapo Tofu)"):
        st.write("**Deskripsi:** Hidangan lembut, pedas, dan bergaya oriental.")
        st.markdown("""
        **Bahan:** 2 tahu sutra (dadu), 100g daging cincang, saus sambal, saus tiram, minyak wijen, maizena.
        
        **Langkah:**
        1. Tumis baput, jahe, & daging.
        2. Masukkan saus & sedikit air.
        3. Masukkan tahu sutra perlahan.
        4. Kentalkan dengan larutan maizena.
        """)
        st.link_button("📺 Tonton Tutorial di YouTube", "https://youtu.be/_NICwQILeTo?si=hDlnmpH_Q3R-DamX")

elif menu == "Cara Menyimpan Tahu":
    st.header("🧊 Tips Penyimpanan Tahu")
    st.warning("Tahu mudah basi karena kadar airnya tinggi. Gunakan cara ini agar awet hingga 1 minggu.")
    
    st.subheader("1. Cuci & Bersihkan")
    st.write("Cuci tahu dengan air mengalir untuk menghilangkan lendir dan bau asam.")
    
    st.subheader("2. Rendam Air Matang")
    st.info("Simpan dalam wadah tertutup. Pastikan tahu terendam sepenuhnya dalam air matang yang sudah dingin.")
    
    st.subheader("3. Perawatan di Kulkas")
    st.write("Simpan di chiller. **Wajib ganti airnya setiap hari** agar bakteri tidak berkembang.")
    
    st.subheader("4. Trik Merebus")
    st.write("Rebus tahu 2-3 menit sebelum disimpan untuk tekstur yang lebih kokoh dan lebih higienis.")

# --- Footer ---
st.divider()
st.caption("Dibuat dengan Python & Streamlit | 2026")
