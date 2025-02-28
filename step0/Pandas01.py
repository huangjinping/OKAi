import pandas as pd

if __name__ == '__main__':
    pass
    print("====pandas01=====")
    df = pd.read_excel('../res/excel/persion_all.xlsx')
    # print(df)
    # print(type(df))
    # grouped = df.groupby("现月度工资").sum()
    total_salary = df['现月度工资'].sum()
    print("现月度工资总金额:", total_salary)

    # 输出结果
    # print("原始数据：")
    # print(df)
    # print("\n按产品类别分组后的总销售额：")
    # print(grouped)

    front_hall_managers = df[df['职务'] == '前厅经理']
    # 找出“现月度工资”列的最大值及其对应的行
    max_salary_row = front_hall_managers.loc[front_hall_managers['现月度工资'].idxmax()]

    # 提取相关信息
    name = max_salary_row['姓名']
    email = max_salary_row['电子邮件']
    department = max_salary_row['部门']
    hire_date = max_salary_row['入职日期']
    position = max_salary_row['职务']
    position_series = max_salary_row['职务序列']
    level = max_salary_row['职级']
    max_salary = max_salary_row['现月度工资']

    # # 输出结果
    # print("职务为'前厅经理'的最高现月度工资信息如下：")
    # print(f"姓名: {name}")
    # print(f"电子邮件: {email}")
    # print(f"部门: {department}")
    # print(f"入职日期: {hire_date}")
    # print(f"职务: {position}")
    # print(f"职务序列: {position_series}")
    # print(f"职级: {level}")
    # print(f"现月度工资: {max_salary}元")
    #
    # # 确保“现月度工资”列是数值类型，处理可能的非数值数据
    # df['现月度工资'] = pd.to_numeric(df['现月度工资'], errors='coerce')
    #
    # # 按“职务”分组，并找出每组中“现月度工资”最大的行
    # max_salary_by_position = df.loc[df.groupby('职务')['现月度工资'].idxmax()]
    #
    # # 重置索引以便更容易处理
    # max_salary_by_position = max_salary_by_position.reset_index(drop=True)
    #
    # # 输出结果
    # print("各个职务中月度工资最高的人员信息如下：")
    # for index, row in max_salary_by_position.iterrows():
    #     print(f"\n职务: {row['职务']}")
    #     print(f"姓名: {row['姓名']}")
    #     print(f"电子邮件: {row['电子邮件']}")
    #     print(f"部门: {row['部门']}")
    #     print(f"入职日期: {row['入职日期']}")
    #     print(f"职务序列: {row['职务序列']}")
    #     print(f"职级: {row['职级']}")
    #     print(f"现月度工资: {row['现月度工资']}元")
    #     print("-" * 50)