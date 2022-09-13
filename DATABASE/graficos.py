import tkinter as tk

escala_grafica = 1
n_cordas = 6

h_entre_cordas = 10 * escala_grafica
w_tarracha = 3 * h_entre_cordas

# dimencoes horizontais
w_cabeca = (((n_cordas // 2 + n_cordas % 2) * w_tarracha) + w_tarracha)
w_pescoco = (w_tarracha)
w_pestana = (h_entre_cordas/2)

# dimencoes verticais
x_origem = (2 * w_tarracha)
x_cabeca_ini = (x_origem + w_tarracha)
x_cabeca_fim = (x_cabeca_ini + w_cabeca)
x_pescoco_ini = (x_cabeca_fim)
x_pescoco_fim = (x_pescoco_ini + w_tarracha)
x_pestana_ini = (x_pescoco_fim)
x_pestana_fim = (x_pestana_ini + w_pestana)

# dimensoes verticais
h_braco = (n_cordas * h_entre_cordas)
h_cabeca = (h_braco + w_tarracha)
h_pestana = (h_braco)

# posicoes verticais
y_origem = (x_origem)
y_cabeca_ini = (y_origem)
y_cabeca_fim = (y_cabeca_ini + h_cabeca)
y_pescoco_sup_ini = (y_cabeca_ini)
y_pescoco_sup_fim = (y_cabeca_ini + w_tarracha/2)
y_pescoco_inf_ini = (y_cabeca_fim)
y_pescoco_inf_fim = (y_cabeca_fim - w_tarracha/2)
y_pestana_ini = (y_pescoco_sup_fim)
y_pestana_fim = (y_pestana_ini + h_pestana)

# Canvas dimensions
cvs_width = x_pestana_fim + x_origem
cvs_height = y_pestana_fim + y_origem

# test
app = tk.Tk()
cvs = tk.Canvas(app, width=cvs_width, height=cvs_height, bg='white')
cvs.pack(fill='both', expand=1)

lh_cabeca_ini = cvs.create_line(x_cabeca_ini, y_cabeca_ini, x_cabeca_fim, y_cabeca_ini)
lh_cabeca_fim = cvs.create_line(x_cabeca_ini, y_cabeca_fim, x_cabeca_fim, y_cabeca_fim)
lv_cabeca_ini = cvs.create_line(x_cabeca_ini, y_cabeca_ini, x_cabeca_ini, y_cabeca_fim)

sq_pestana_ini = cvs.create_rectangle(x_pestana_ini, y_pestana_ini, x_pestana_fim, y_pestana_fim)

ls_pescoco = cvs.create_line(x_pescoco_ini, y_pescoco_sup_ini, x_pescoco_fim, y_pescoco_sup_fim)
li_pescoco = cvs.create_line(x_pescoco_ini, y_pescoco_inf_ini, x_pescoco_fim, y_pescoco_inf_fim)



app.mainloop()