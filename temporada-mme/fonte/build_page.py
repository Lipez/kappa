import json,glob,os,base64,sys
prog={}
for f in glob.glob('dbdump/progresso/*.json'):
    d=json.load(open(f)); d=d.get('data',d)
    prog[os.path.basename(f)[:-5]]={k:d.get(k) for k in ['descritivo','seo','cadastro','atualizadoEm'] if k in d}
data=open('data.json').read().replace('</','<\\/')
src=open('/home/user/kappa/temporada-mme/fonte/template.html').read().replace('__DATA__',data)
b64=base64.b64encode(src.encode()).decode()
pj=json.dumps(prog,ensure_ascii=False).replace('<','\\u003c')
out=src.replace('__SRC__',b64,1).replace('__PROGRESS__',pj,1)
open('/home/user/kappa/temporada-mme/painel-anuncios.html','w').write(out)
print(prog, len(out)//1024,'KB')
