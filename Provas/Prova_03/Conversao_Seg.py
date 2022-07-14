# Ex: 89450 é pra dá 24h, 50min e 50s.
def converter_seg(s):
  h_s = s / 3600
  ss = s % 3600
  m_s = ss / 60
  ss = ss % 60
  return print(f"{int(h_s)}h, {int(m_s)}min e {int(ss)}s.")

s = int(input("S: "))
converter_seg(s)