# German-Scene-Dataset
# How to obtain the data
Since the novels are protected by copyright, we cannot publish them directly. Instead, you will find the segmentation in standoff format. To work with the data set you have to buy the novels listed below. Then name the epub files after their EAN/ISBN to create this folder structure:
* epubs (main folder) <br> 
  * 9783740950484.epub <br>
  * 9783845397535.epub <br>
  * 9783732515684.epub <br>
  * 9783732517695.epub <br>
  * ... <br>
  
 Next run create_dataset.py to merge epubs and standoff annotations from gold.json.<br>
 This will store a json file for each novel in a new folder ./scene-dataset. <br>
 
 JSON Layout: <br>
 ["text"]: Raw text <br>
 ["scences"]: List of dictionaries contationing "start" and "end" character positions for scenes <br>
 
## Requirements
python >= 3.8 <br>
ebooklib EbookLib >= 0.17.1
# Novels
* Patricia Vandenberg: "Die hochmütigen Fellmann-Kinder." Sophienlust Classic 9. Matin Kelter Verlag EAN: 9783740950484 <br>
* Hugh Walker: "Der Sohn des Kometen." Mythor Bd.1. Pabel Moewig Verlag. ISBN-13: 9783845397535 <br>
* Wolfgang Hohlbein: "Als der Meister starb." Der Hexer Bd.2. Bastei Lübbe.  EAN: 9783838721675 <br>
* Jason Dark: "Der Turm der 1000 Schrecken". John Sinclair Bd. 32. Bastei Lübbe Horror EAN: 9783838727868 <br>
* Regine König: "Bezaubernde neue Mutti". Fürstenkinder Bd.8. Martin Kelter Verlag. EAN: 9783740965716 <br>
* Frank Rehfeld: "Hetzjagd durch die Zeit." Dino-Land Bd.5. Bastei Lübbe. EAN: 9783732535200 <br>
* O. S. Winterfield: "Immer wenn der Sturm kommt." Die schwarzen Perlen Bd.27. Bastei Lübbe. EAN: 9783732517695 <br>
* Verena Kufsteiner: "Lass Blumen sprechen." Das Berghotel Bd.210. Bastei Lübbe. EAN: 9783732591732 <br>
* Marina Anders: "Ein Weihnachtslied für Dr. Bergen." Notärztin Andrea Bergen Bd.1341. Bastei Lübbe. EAN: 9783732557905 <br>
* Manfred Weinland: "Prophet der Apokalypse". 2012 Bd.6. Bastei Lübbe. EAN: 9783838713625 <br>
* Frank Callahan: "Die Abrechnung." Skull Ranch Bd.29. Bastei Lübbe. EAN: 9783732597314 <br>
* G.F. Unger: "Tausend Pferde." G.F. Unger Sonder-Edition Bd.187. Bastei Lübbe. ISBN-13: 9783732596249. <br>
* Hedwig Courths-Mahler: "Verschmäht." Hedwig Courths-Mahler Bd.50. Bastei Lübbe. EAN: 9783732502929 <br>
* Andreas Kufsteiner: "Wechselhaft wie der April." Der Bergdoktor Bd.2018. Bastei Lübbe. EAN: 9783732591725  <br>
* Friederike von Bucher: "Wir schaffen es - auch ohne Mann." Toni der Hüttenwirt Bd.223. EAN: 9783740941093  <br>

# Paper
Link to paper
