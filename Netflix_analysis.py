import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_excel("Netflix_analysis.xlsx")

df.dropna(subset= ["director", "country"] ,inplace=True)

df.replace({
    "country" : {"Unknown" : "Pakistan"},
    "director" : {"Not Specified" : "Zeeshan"},
    "cast" : {"Not Specified" : "Ahmad"}   
}, inplace=True)
print(df)

country_count = df[df["country"] == "United States"]["director"].value_counts().head(3).copy()
duration_count = df[df["country"] == "India"].copy()
duration_count["int_duration"] = duration_count["duration"].str.replace("min", "").str.replace("Seasons", "").str.replace("Season","").astype(int)
year_count = df["release_year"].value_counts().sort_index().copy()
country_comp = df["country"].value_counts().head(5)

fig, axs = plt.subplots(2,2, figsize=(10,7))

#bar
axs[0,0].bar(country_count.index, country_count.values, color= ["red", "green", "blue"], edgecolor="black", linewidth=1.2)
axs[0,0].set_xlabel("United States directors")
axs[0,0].set_ylabel("No of movies")
axs[0,0].grid(color="grey", linestyle=":")

#hist
axs[0,1].hist(duration_count["int_duration"], bins=10, color="red", edgecolor="black", linewidth=1.2)
axs[0,1].set_xlabel("Indian movies duration")
axs[0,1].set_ylabel("No of movies in India")
axs[0,1].grid(color="grey", linestyle=":")

#scatter
axs[1,0].scatter(year_count.index, year_count.values, color="yellow", edgecolor="black", linewidth=1.2)
axs[1,0].set_xlabel("year")
axs[1,0].set_ylabel("Movies")
axs[1,0].grid(color="grey", linestyle=":")

#pie
axs[1,1].pie(country_comp.values, labels=country_comp.index, autopct="%1.1f%%", colors=["red", "blue", "green", "yellow", "orange"], explode=[0.1,0,0,0,0], shadow=True, startangle=140)





plt.suptitle("Netflix analysis", fontsize=16)
plt.tight_layout()
plt.savefig("Netflix Analysis.png", dpi=300 )
plt.show()



