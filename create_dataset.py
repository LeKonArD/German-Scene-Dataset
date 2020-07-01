import os
import json
import re
import html as cleaner
import ebooklib
from ebooklib import epub


def create_corpus(borders, gold):
    
    for ean in list(borders.keys()):
        
        path = 'epubs/'+str(ean)+'.epub'
        book = epub.read_epub(path)
        html = ""
        
        for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            if borders[ean][3] == False:
                txt = re.sub("<[^>]+>","",doc.content.decode("utf8"))
            else:
                txt = re.sub("<[^>]+>","",cleaner.unescape(doc.content.decode("utf8")))
            txt = re.sub("\t","",txt)
            html+=txt
            
        thtml = html[borders[ean][0]:borders[ean][1]]
        p = re.sub("\&[^\;]+\;"," ",thtml)
        p = re.sub("\n"," ",p)
        p = re.sub("\s+"," ",p)
        p = re.sub("\t+","",p)
        
        if borders[ean][2] == None:
            pass
        else:
            for replacment in borders[ean][2]:
              
                p = re.sub(replacment[0], replacment[1], p)
        
        
        output = {}
        output["scenes"] = gold[str(ean)]
        output["text"] = p 
        with open('scene-dataset/'+str(ean)+".json", 'w') as outfile:
               json.dump(output, outfile)
        

borders = {
    9783732535200:[1232,196089,[["»Graben\?«","» Graben?«"]],False],
    9783732517695:[834,193211,[["von O. S. Winterfield ",""],["Die Schwarzen Perlen ",""]],False],
    9783732502929:[875,201946,None,False],
    9783732591732:[747,150218,None,True],
    9783838713625:[1050,162290,[["Prophet der Apokalypse ",""]],True],
    9783845397535:[4742,168971,[["[0-9]\. [0-9]\.","1."]],True],
    9783740965716:[758,171243,[["\* ", ""],["\.\.", ". ."],["Luft. Denn G","Luft. D enn G"]],True],
    9783740950484:[882,195539,[["\* ", ""]],True],
    9783732597314:[1246,150983,None,True],
    9783732557905:[831,170777,[["… Andrea Bergen ", "… "]],True],
    9783740941093:[879,157354,None,True],
    9783838727868:[1049,159415,[["r allein … \* Es war ","r allein …Es war "],["Eine fette schwarze Spinne ließ sich von der Decke hinab und baumelte vor Carlas Augen hin und her.Fledermäuse mit dolchartigen Zähnen und weit aufgerissenen Mäulern flatterten lautlos durch das Verlies.Ein Skelett streckte ihr zur Begrüßung die Hand entgegen; seine Knochen klapperten.Carla spürte den kalten Hauch des Todes. Wie von Sinnen schrie sie, bis ihr die Stimme versagte … John Sinclair - Folge 0032",
           "Eine fette schwarze Spinne, ließ sich von der Decke herab und tänzelte vor Carlas Augen hin und her. Fledermäuse mit dolchartigen Zähnen und weit aufgerissenen Mäulern flatterten. lautlos durch das Verlies. Ein Skelett streckte Carla zur Begrüßung die Hand entgegen. Seine Knochen klapperten. Carla spürte den kalten Hauch des Todes. Wie von Sinnen schrie sie, bis ihr die Stimme versagte …"]],True],
    9783732596249:[1468,230821,None,True],
    9783732591725:[692,148325,[["Korbinian, stand auf dem Display.","Korbinian , stand auf dem Display."],["Korbinian erkennt seine junge Fraunicht wieder Von Andreas Kufsteiner ",
           "Korbinian erkennt seine junge Frau\n                \n                \n                \n                nicht wieder\n                \n                \n                \n                Von Andreas Kufsteiner "]],True],
    9783838721675:[6177,406653,[["sagte Andara verzweifelt","s agte Andara verzweifelt"],
                                ["schrie Andara. Verzweifelt","s chrie Andara. Verzweifelt"],
                               ["sagte Roderick beschwörend.","s agte Roderick beschwörend."],
                               ["Handvoll","Hand voll"],
                               ["schrie Necron","s chrie Necron"]],True]
}


if not os.path.isdir('scene-dataset'):
    os.makedirs('scene-dataset')

gold = json.loads(open("gold.json","r").read())
print(len(gold.keys()))   
create_corpus(borders, gold)   
