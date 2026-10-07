import csv

# อ่านข้อมูลจากไฟล์ txt (ไฟล์เป็นรูปแบบ CSV: ชื่อ, คุณสมบัติ, พฤติกรรม)
def load_waste(filename):
    items = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            if len(row) != 3:  
                continue
            name, kind, state = [x.strip() for x in row]
            items.append({"name": name, "type": kind, "state": state})
    return items

bins = {
    "recycle": "ถังเหลือง (รีไซเคิล)",
    "general": "ถังน้ำเงิน (ขยะทั่วไป)",
    "hazardous": "ถังแดง (ขยะอันตราย)",
}

def classify(item):
    # ขยะรีไซเคิลที่เปื้อน ล้างไม่ได้ ให้ทิ้งเป็นขยะทั่วไป
    if item["type"] == "recycle" and item["state"] == "dirty":
        return "general"
    return item["type"]

def main():
    items = load_waste("ประเภทขยะ.txt")

    # แสดงผลการแยกขยะทั้งหมด
    for it in items:
        b = classify(it)
        print(f"{it['name']:<30} -> {bins[b]}")

    # สรุปจำนวนแต่ละประเภท
    count = {k: 0 for k in bins}
    for it in items:
        count[classify(it)] += 1
    print("\nสรุป")
    for k, v in count.items():
        print(f"{bins[k]}: {v} ชิ้น")


main()

#สัปดาห์ที่ 2 แยกขยะแต่ยังไม่มี interaction + ส่งด้วย git hub

