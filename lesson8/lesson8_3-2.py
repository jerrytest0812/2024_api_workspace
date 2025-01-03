from tools import get_youbikes
import streamlit as st

youbike_data:list[dict] = get_youbikes()

# 使用streamlit分2個欄位
# 使用you_bike_data:list的資料, 取出所有的行政區域(sarea), 不可以重複
# 左邊是選擇行政區域(sarea), 使用下拉式表單
# 右邊是顯示該行政區域的YouBike站點資訊的表格資料
# 最下方是顯示該行政區域的YouBike站點資訊的地圖
sarea_list = sorted(set(map(lambda item:item['sarea'],youbike_data)))
col1,col2 = st.columns([1,4])
with col1:
    selected_arear = st.selectbox("顯示行政區", sarea_list)
with col2:
    def filter_func(value:dict)->bool:
        return value['sarea'] == selected_arear
       
    filter_list:list[dict] = list(filter(filter_func,youbike_data))
    show_data:list[dict] = [{
            "站點":item['sna'],
            "總車輛數":item['tot'],
            "可借車輛數":item['sbi'],
            "可還車輛數":item['bemp'],
            "營業中":item['act'],
            "latitude":float(item['lat']),
            "longitude":float(item['lng'])
            } for item in filter_list]
    st.dataframe(show_data,width=800)

    # 生成該行政區站點資訊地圖於下方

    st.map(show_data,latitude='latitude',longitude='longitude')




# #顯示地圖
# filter_data = list(filter(lambda item:item['sarea'] == selected_sarea,youbike_data))
# locations = [{'lat': float(item['lat']), 'lon': float(item['lng'])} for item in filter_data]
# st.map(locations)