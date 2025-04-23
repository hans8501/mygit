import pandas as pd
import glob
import os

# 엑셀 파일들이 저장된 폴더 경로
folder_path = '/Users/suminhan/Downloads/Factor6_Data/Merged'

# 엑셀 파일들 모두 찾기 (확장자가 xlsx인 경우)
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

# 파일들을 하나씩 읽고 합치기
merged_df = pd.DataFrame()

for file in excel_files:
    df = pd.read_excel(file)
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# 하나의 파일로 저장
output_path = os.path.join(folder_path, 'Total_merged_output.xlsx')
merged_df.to_excel(output_path, index=False)