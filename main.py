def main():
    map, altezza = load()
    viste, posizoni = calc(map, altezza)
    for i in range(len(viste)):
        for l in range(len(viste) - i -1):
            if int(viste[l+1]) > int(viste[l]):
                (viste[l+1], viste[l]) = (viste[l], viste[l+1])
                posizoni[l+1], posizoni[l] = posizoni[l], posizoni[l+1]
    
    count = 1
    for i in viste:
        print(count,"\t",posizoni[count-1] ,": Valore = ", viste[count-1])
        count += 1
    
def calc(map: list, altezza):
    viste = []
    posizioni = []
    lunghezza = 0
    for i in map[0]:
        lunghezza += 1
    lunPos = 0
    altPos = 0
    for l in map:
        for i in l:
            if altPos==0:
                if lunPos==0:
                    val = (int(map[0][0]) - int(map[0][1])) + (int(map[0][0]) - int(map[1][0])) + (int(map[0][0]) - int(map[1][1])) + 5*int(map[0][0])
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))
                    #print("Valore in ", altPos, " , " ,lunPos,": ",val)
                    lunPos += 1
                elif lunPos==lunghezza-1:
                    val = 0
                    ed = int(map[altPos][lunPos])
                    val += (ed- int(map[altPos][lunPos-1]))
                    val += (ed - int(map[altPos+1][lunPos-1])+ (ed-int(map[altPos+1][lunPos])))
                    val += ed*5
                    #print("Valore in ", altPos, " , ", lunPos,": ",val)
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))
                    lunPos=0
                    altPos += 1
                else:
                    val = 0
                    ed = int(map[altPos][lunPos])
                    val += (ed-int(map[altPos][lunPos-1])) + (ed-int(map[altPos][lunPos +1]))
                    val += (ed-int(map[altPos+1][lunPos-1])) + (ed-int(map[altPos+1][lunPos])) + (ed-int(map[altPos+1][lunPos+1]))
                    val += ed*3
                    #print("Valore in ", altPos, " , ", lunPos,": ",val)
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))
                    #print(map[altPos][lunPos])(ma
                    lunPos +=1
            elif altPos == altezza-1:
                if lunPos==0:
                    val = 0
                    ed = int(map[altPos][lunPos])
                    val += (ed-int(map[altPos-1][lunPos]) + (ed-int(map[altPos-1][lunPos+1])))
                    val += (ed-int(map[altPos][lunPos+1]))
                    val += ed*5
                    #print("Valore in ", altPos, " , ", lunPos,": ",val)
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))
                    lunPos+=1
                elif lunPos==lunghezza-1:
                    ed = int(map[altPos][lunPos])
                    val = 0
                    val += (ed-int(map[altPos-1][lunPos]))+ (ed-int(map[altPos-1][lunPos-1]))
                    val += (ed-int(map[altPos][lunPos-1]))
                    val += ed*5
                    #print("Valore in ", altPos, " , ", lunPos,": ",val)
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))

                    lunPos=0
                    altPos+=1
                else:
                    val = 0
                    ed = int(map[altPos][lunPos])
                    val += (ed-int(map[altPos][lunPos-1])) + (ed-int(map[altPos][lunPos +1]))
                    val += (ed-int(map[altPos-1][lunPos-1])) + (ed-int(map[altPos-1][lunPos])) + (ed-int(map[altPos-1][lunPos+1]))
                    val += ed*3
                    #print("Valore in ", altPos, " , ", lunPos,": ",val)
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))
                    lunPos +=1
            else:
                if lunPos==0:
                    ed = int(map[altPos][lunPos])
                    val = (ed - int(map[altPos-1][lunPos])) + (ed - int(map[altPos-1][lunPos+1]))
                    val += (ed - int(map[altPos][lunPos +1]))
                    val += (ed - int(map[altPos+1][lunPos+1]) + (ed - int(map[altPos+1][lunPos])))
                    val += ed*3
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))
                    #print("Valore in ", altPos, " , ", lunPos,": ",val)
                    
                    lunPos += 1
                elif lunPos==lunghezza-1:
                    val = 0
                    ed = int(map[altPos][lunPos])
                    val += (ed- int(map[altPos-1][lunPos]) + (ed- int(map[altPos-1][lunPos-1])))
                    val += (ed- int(map[altPos][lunPos-1]))
                    val += (ed - int(map[altPos+1][lunPos-1])+ (ed-int(map[altPos+1][lunPos])))
                    val += ed*3
                    #print("Valore in ", altPos, " , ", lunPos,": ",val)
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))
                    lunPos=0
                    altPos += 1
                else:
                    val = 0
                    ed = int(map[altPos][lunPos])
                    val += (ed-int(map[altPos-1][lunPos-1])) + (ed-int(map[altPos-1][lunPos])) + (ed-int(map[altPos-1][lunPos+1]))
                    val += (ed-int(map[altPos][lunPos-1])) + (ed-int(map[altPos][lunPos+1]))
                    val += (ed-int(map[altPos+1][lunPos-1])) + (ed-int(map[altPos+1][lunPos])) + (ed-int(map[altPos+1][lunPos+1]))
                    #print("Valore in ", altPos, " , ", lunPos,": ",val)
                    viste.append(str(val))
                    posizioni.append((altPos, lunPos))
                    lunPos +=1
                
    #print(viste)
    #print(posizioni)
    return viste, posizioni
                
def load():
    map = []
    altezza = 0
    try:
        data = open("mappa.txt", "r")
        for l in data.readlines():
            linea = l.rstrip()
            altezza += 1
            map.append(linea)
    except Exception as e:
        print("Error ", e)
    return map, altezza

main()
