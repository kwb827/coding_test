# key = seq의 기준으로 잡을 컬럼
# key2 = seq의 부기준으로 잡을 컬럼

# ex)
# key   key2    seq
# 1     1       1_1
# 1     1       1_1
# 1     2       1_2
# 1     3       1_3
# 2     1       2_1
# 2     1       2_1
# 2     2       2_2

def sequence(df,key,ket2) :
    seq = 1
    key_seq = key+'_seq'
    df[key_seq] = '0_0'

    for i in range(0, len(df)):
        if i == 0:
            df.iloc[i, df.columns.get_indexer([key_seq])] = str(
                df[key][i]) + '_' + str(seq)
            continue

        if df.loc[i, ket2] != df.loc[i - 1, ket2]:
            seq += 1

        if df.loc[i, key] != df.loc[i - 1, key]:
            seq = 1

        df.iloc[i, df.columns.get_indexer([key_seq])] = str(
            df[key][i]) + '_' + str(seq)

    return df