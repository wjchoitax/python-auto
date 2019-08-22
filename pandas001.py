import pandas as pd

# df = pd.read_excel('not-paid.xlsx', sheet_name='미결제 명단')

df = pd.read_csv('C:\\Users\\KITRI\\Desktop\\examples\\05\\csv_files\\2017.01.csv')

new_df = df.loc[df['수강금액'] >= 800000]

new_df.to_excel('고액수강생.xlsx', index=False)

print('save ok..')

