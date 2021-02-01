import pandas as pd
import os

file = open("./static/txt/imglink.txt", "r")
contents = file.read()
file.close()
imglink_list = list(filter(None, contents.split("\n")))

Header = {"Product_link": imglink_list}
df = pd.DataFrame(Header, columns=["Product_link"])

df.to_csv(r"./static/csv/mnfurniture_dataframe.csv", index=False, header=True)
