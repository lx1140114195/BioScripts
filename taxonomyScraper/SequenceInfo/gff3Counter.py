import pprint
from BCBio.GFF import GFFExaminer
def counter(f,acces):
    in_file = f
    examiner = GFFExaminer()
    in_handle = open(in_file)
    # pprint.pprint(examiner.available_limits(in_handle))
    dic = examiner.available_limits(in_handle)
    # pprint.pprint(dic['gff_type'])
    dicgff = dic['gff_type']
    getThis = ['CDS','rRNA','tRNA']
    cds = dic['gff_type'][('CDS',)]
    rrna = dic['gff_type'][('rRNA',)]
    trna = dic['gff_type'][('tRNA',)]
    newdic = {acces : {'CDS': cds, 'rRNA' : rrna, 'tRNA' : trna }}
    in_handle.close()
    return newdic

            
