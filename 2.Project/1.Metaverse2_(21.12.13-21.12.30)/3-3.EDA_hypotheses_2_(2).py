
#



landmark_pre = pd.read_csv("3.최종 예상랜드.csv", encoding = "cp949")
land_tree_pre = pd.read_csv("4.예상랜드구_산,강 토탈.csv", encoding = "cp949")

# 서울 전체 TP 중, 예상 랜드마크가 차지하는 점유율 약 5%
landmark_pre["TP_원"].sum() / df_meta["totalPrice"].sum() * 100

# 서울 전체 면적 중, 랜드마크가 차지하는 점유율 약 0.33%
landmark_pre["타일 수"].sum() / (3025000) * 100


#확정랜드마크에 비해 상대적으로 메타버스2 가상부동산 가격형성에 미치는 영향이 적지만,
#면적대비 TotalPrice가 차지하는 비율이 약 16배 높은 것으로 확인됨
#그러므로, 약간의 기대심리가 반영된 것으로 보임
