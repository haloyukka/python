import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

# write() -> 表の細かい設定はできない
# dataframe() -> 表の縦横の長さを指定できる
# dataframe() -> 「動的」なテーブルを使いたい時
# table() -> 「静的」なテーブルを使いたい時

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)
# st.table(df)

# markdownを埋め込める

# # 章
# ## 節
# ### 項

# ``` python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```



# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a','b','c']
# )
# # st.line_chart(df)
# # st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/ [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

st.write('Display Image')

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='はい。かわいい', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    options=list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'
