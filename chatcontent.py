import neologdn
import emoji

for i, line in enumerate(lines):
    # 西暦の行を削除
    if ('2018' in line) or ('2019' in line) or ('2020' in line):
        line = ''
    # 会話でないものを削除
    elif ('[スタンプ]' in line) or ('[ファイル]' in line) or ('[写真]' in line) or ('[動画]' in line) or ('アルバム' in line) or ('ノートに' in line) or ('通話' in line) or ('http' in line):
        line = ''
    # 時刻を削除
    if len(line) >= 4:
        if line[1] == ':':
            line = line[4:]
        elif line[2] == ':':
            line = line[5:]
    # 表現を正規化
    line = neologdn.normalize(line)
    # 絵文字を除去
    line = ''.join(['' if c in emoji.UNICODE_EMOJI else c for c in line])

# リストから空の文字列を削除
lines = list(filter(lambda a: a != '', lines))

# どちらの発言かを判定しリストに格納
my_name='hoge男'
partner_name='huge子'

my_remarks=[]
partner_remarks=[]

for line in lines:
    if line[0:3]==my_name[0:3]:
        speaker=my_name
        my_remarks.append(line.replace(my_name,''))

    elif line[0:3]==partner_name[0:3]:
        speaker=partner_name
        partner_remarks.append(line.replace(partner_name,''))

    else:
        if speaker==my_name:
            my_remarks.append(line.replace(my_name,''))
        else:
            partner_remarks.append(line.replace(partner_name,''))

my_remarks_file_path = './../data/my_remarks.txt'
partner_remarks_file_path = './../data/pa_remarks.txt'

# 自分の発言をtxtファイルに書き込み
with open(my_remarks_file_path, mode='w') as f:
    f.write('\n'.join(my_remarks))

# 相手の発言をファイルに書き込み
with open(partner_remarks_file_path, mode='w') as f:
    f.write('\n'.join(partner_remarks))