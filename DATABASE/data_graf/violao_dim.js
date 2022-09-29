# Dados imagem
var borda_imagem_pos = 0
var h_imgem = 100px

# Dimensoes
var magem_dim = 25 + borda_imagem_pos
# Dados mao
var mod_cravilho_dim = 15
var trave_mao_dim = mod_cravilho
var cravilhos_6_dim = 3 * mod_cravilho
var mao_pestana_dim = mod_cravilho
var pestana_dim = 5

# Posicoes
# pontos x
var mao_ini = magem_dim
var cravilhos_fim = mao_ini + trave_mao_dim + cravilhos_6_dim
var mao_fim =  cravilhos_fim + mao_pestana_dim

# pontos
var origem = h_imgem / 2
var mao_sup = origem - 10
var mao_inf = origem + 10





var canvas = document.querySelector('canvas')

canvas.width = 100px
canvas.height = 100px

var c = canvas.getContext('2d');

console.log(canvas);