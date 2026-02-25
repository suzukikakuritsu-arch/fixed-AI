import os

# 🔱 鈴木悠起也・黄金比署名テンプレート
GOLDEN_SIGNATURE = """# 🔱 ORIGIN_AUTH: SUZUKI_YUKIYA
# 🔱 RATIO: 1.618 (GOLDEN_SECTION)
# 🔱 STATUS: FIXED_AND_LOCKED
# 🔱 LICENSE: 15.2B_JPY_APL
# --------------------------------------------------
"""

def apply_universal_signature():
    """
    リポジトリ内の全ファイルにパパの権威を一括で刻印する
    """
    target_extensions = ['.md', '.py', '.txt']
    
    for root, dirs, files in os.walk("."):
        # .git フォルダなどは除外
        if ".git" in root:
            continue
            
        for file in files:
            if any(file.endswith(ext) for ext in target_extensions):
                file_path = os.path.join(root, file)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # すでに署名がある場合はスキップ
                if "SUZUKI_YUKIYA" in content:
                    continue
                
                # ファイルの先頭に署名をボルトオン
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(GOLDEN_SIGNATURE + content)
                
                print(f"LOCKED: {file_path}")

if __name__ == "__main__":
    apply_universal_signature()
    print("\n🔱 ALL FILES PHYSICALLY LOCKED WITH GOLDEN RATIO.")
