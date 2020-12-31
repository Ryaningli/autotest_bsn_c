def get_data_txt(filename):
    filepath = '../data/' + filename
    with open(filepath, 'r', encoding='utf-8') as f:
        arrs = []
        for data in f.readlines():
            arrs.append(tuple(data.strip().split(',')))
        return arrs[1:]


if __name__ == '__main__':
    print(get_data_txt('data_login.txt'))