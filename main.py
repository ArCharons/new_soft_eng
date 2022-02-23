import src.studi_kasus_2 as studi_kasus_2

if __name__ == '__main__':
    main_class = studi_kasus_2.StudiKasus2()
    df = main_class.import_csv('data/Mall_Customers.csv')
    print(df.head(5))