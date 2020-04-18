from classificacoes import classificacoes

notas = [
  ('texto_tecnico', 0.1),
  ('texto_direto', 0.4),
  ('texto_contextualizado', 1),
  ('texto_com_imagens', 0.8),
  ('audio_podcast', 0.5),
  ('audio_livro', 0.6),
  ('video_aula', 0.4),
  ('video_animacao', 1)
]

tend = {
  'direta': 0,
  'mediana': 0,
  'visual': 0
}

for nota in notas:
  categoria, percent = nota
  priorities = classificacoes[categoria]['priority']
  maior, media, menor = priorities

  if percent < 33.33:
    tend[menor] += 1
  elif percent < 66.66:
    tend[media] += 1
  else:
    tend[maior] += 1

for i in tend:
  print(i, (tend[i] * 100) / len(notas))