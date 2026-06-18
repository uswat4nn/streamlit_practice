import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# load data
def load_data():
    df = pd.read_csv("spotify.csv")
    df = df.dropna()
    return df

df = load_data()

# # title
# st.title("Spotify Data Dashboard")
# st.subheader("Analisis data musik pada Spotify")

# # logo
# LOGO = "logo.png"

# col1, col2 = st.columns([5,1])

# with col1:
#     st.title("Spotify Data Dashboard")
#     st.subheader("Analisis data musik pada Spotify")

# with col2:
#     st.image("logo.png", width=100)

# # sidebar
# st.sidebar.image(LOGO, width=200)

# # filter(konten)
# selected_album = st.sidebar.selectbox("Pilih tipe album", options=df["album_type"].unique())
# filterdf = df[df['album_type'] == selected_album]

# HEADER (judul + logo kanan)
col1, col2 = st.columns([5,1])

with col1:
    st.title("Spotify Data Dashboard")
    st.subheader("Analisis data musik pada Spotify")

with col2:
    st.image("logo.png", width=100)

# FILTER DI BAWAH JUDUL
selected_album = st.selectbox(
    "Pilih tipe album",
    options=df["album_type"].unique()
)

filterdf = df[df['album_type'] == selected_album]

# preview data 100 rows (menampilkan tabel yang berisi 100 data)
st.subheader("Data Preview")
st.dataframe(filterdf.head(100))

# distribusi top 10 artist
st.subheader("Distribusi Top 10 Artist")
top_artists = filterdf['artist_name'].value_counts().head(10)
fig1, ax1 = plt.subplots()
top_artists.plot(kind='bar', ax=ax1)
st.pyplot(fig1)


# proporsi lagu explicit vs non explicit
st.subheader("Proporsi Lagu Explicit vs Non Explicit")

type_counts = df["explicit"].value_counts()

fig1, ax1 = plt.subplots()
type_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax1)

#ax1.set_title("Proporsi Lagu Explicit vs Non Explicit")
ax1.set_ylabel("explicit")

st.pyplot(fig1)

# history popularity
st.subheader("History Lagu Popular") 
fig3, ax3 = plt.subplots()
ax3.hist(filterdf['track_popularity'], bins=10) 
st.pyplot(fig3)

# distribusi top 10 genres
st.subheader("Distribusi Top 10 Genres")

genre_counts = filterdf['artist_genres'].value_counts().head(10)

fig1, ax1 = plt.subplots()
genre_counts.plot(kind='bar', ax=ax1)

ax1.set_title(" ")
ax1.set_xlabel(" ")
ax1.set_ylabel("Jumlah")

st.pyplot(fig1)