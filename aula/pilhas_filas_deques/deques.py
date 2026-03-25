from collections import deque

historico = deque()

historico.append("Google")
historico.append("Youtube")
historico.append("Instagram")
historico.append("Spotify")

pagina = historico.pop()
removida = historico.popleft()

print("Histórico inicial:", historico)

historico.appendleft("TikTok")

print("Histórico final:", historico)
