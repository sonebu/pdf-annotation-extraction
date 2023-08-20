from pypdf import PdfReader
import sys

def main():
    input_filename = sys.argv[1]
    reader = PdfReader(input_filename)
    for i, page in enumerate(reader.pages):
        print("Page", i, "Annotations")
        print("-"*40)
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if(obj["/Subtype"]=="/Popup"):
                    continue
                if((obj["/Subtype"]=="/Caret") and (obj["/Subj"]=="Inserted Text")):
                    print("- Caret, inserted text is: ", obj["/Contents"])
                if(("/IRT" not in obj.keys()) and (obj["/Subj"]=="Cross-Out")):
                    print("- Strikethrough, don't know the location")
                if((obj["/Subtype"]=="/Highlight") and (obj["/Subj"]=="Highlight")):
                    try:
                        print("- Note, text is: ", obj["/Contents"])
                    except:
                        print("- Note, but no text")
        print("")            
        print("")            

if __name__ == "__main__":
    main()