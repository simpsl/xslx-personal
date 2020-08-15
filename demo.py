import csv, os, sys, xlsxwriter

def convert(file_path, file_name):
    if not file_name.endswith('.csv'): return
    header_contents = os.linesep.join(['&L&F', 'Page &P of &N'])
    source_path = os.path.join(file_path, file_name)
    target_path = source_path[:-4] + '.xlsx'
    workbook = xlsxwriter.Workbook(target_path)
    try:
        print('[DEBUG] file path: %s => %s' % (source_path, '.xlsx'), file=sys.stderr)
        w = workbook.add_worksheet('Converted ' + file_name)
        with open(source_path, 'r') as rows:
            w.set_header(header_contents)
            for i, r in enumerate(csv.reader(rows)):
                for j, c in enumerate(r):
                    w.write(i, j, c)
    except Exception as e:
        print(e, file=sys.stderr)
    finally:
        print('[DEBUG] file done', file=sys.stderr)
        workbook.close()

def main(data_name='data', root_path=os.getcwd()):
    data_path = os.path.join(root_path, data_name)
    print('[DEBUG] data path:', data_path, file=sys.stderr)
    for walk_path, dnames, fnames in os.walk(data_path):
        # decend into directories
        # only process .csv files
        for f in fnames:
            convert(walk_path, f)

if __name__ == '__main__':
    main()
