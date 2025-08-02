# Pythonの引数アンパック (`*` と `**` の使い方)

Pythonでは、`*` や `**` を使って関数に引数を渡す際に、リストや辞書をアンパックすることができます。これにより、柔軟な引数の渡し方が可能になります。

---

## 1. 通常の引数渡し (`job`)
- **意味**: 変数をそのまま渡します。
- **用途**: 関数が1つの引数としてリストや辞書を受け取る場合に使用します。

### 例:
```python
job = {"title": "Engineer", "company": "Tech Co"}
Util.print_job_details(job)  # 関数は辞書全体を1つの引数として受け取る
```

---

## 2. アンパック (`*job`)
- **意味**: リストやタプルをアンパックして、複数の位置引数として渡します。
- **用途**: 関数が複数の位置引数を受け取る場合に使用します。

### 例:
```python
job = ["Engineer", "Tech Co", "Remote", "IT"]
Util.print_job_details(*job)  # 各要素が個別の引数として渡される
```

---

## 3. キーワード引数のアンパック (`**job`)
- **意味**: 辞書をアンパックして、キーワード引数として渡します。
- **用途**: 関数がキーワード引数を受け取る場合に使用します。

### 例:
```python
job = {
    "title": "Engineer",
    "company": "Tech Co",
    "head_quater": "Remote",
    "categories": "IT"
}
Util.print_job_details(**job)  # 辞書のキーが引数名、値が引数の値として渡される
```

---

## 違いのまとめ
| 方法       | 対象         | 渡し方の意味                          | 使用例                          |
|------------|--------------|---------------------------------------|---------------------------------|
| `job`      | そのまま      | 1つの引数として渡す                  | `func(job)`                    |
| `*job`     | リスト/タプル | 各要素を位置引数として渡す            | `func(*job)`                   |
| `**job`    | 辞書         | 各キーと値をキーワード引数として渡す  | `func(**job)`                  |

---

## 関数での受け取り方

`job`、`*job`、`**job`を関数で受け取る場合、それぞれの方法に応じた受け取り方と使用方法を以下に示します。

### 1. 通常の引数渡し (`job`)
- **受け取り方**: 引数を1つのオブジェクト（リストや辞書など）として受け取ります。
- **使用方法**: 渡されたオブジェクトをそのまま操作します。

#### 例:
```python
def process_job(job):
    print(f"Job Title: {job['title']}")
    print(f"Company: {job['company']}")

job = {"title": "Engineer", "company": "Tech Co"}
process_job(job)
```

---

### 2. アンパック (`*job`)
- **受け取り方**: 複数の位置引数をタプルとして受け取ります。
- **使用方法**: タプルのインデックスを使って値を操作します。

#### 例:
```python
def process_job(*job):
    print(f"Job Title: {job[0]}")
    print(f"Company: {job[1]}")

job = ["Engineer", "Tech Co"]
process_job(*job)
```

---

### 3. キーワード引数のアンパック (`**job`)
- **受け取り方**: キーワード引数を辞書として受け取ります。
- **使用方法**: キーワード引数の名前を使って値を操作します。

#### 例:
```python
def process_job(**job):
    print(f"Job Title: {job['title']}")
    print(f"Company: {job['company']}")

job = {
    "title": "Engineer",
    "company": "Tech Co"
}
process_job(**job)
```

---

### 違いのまとめ
| 方法       | 受け取り方                     | 使用方法                          |
|------------|-------------------------------|-----------------------------------|
| `job`      | 1つのオブジェクトとして受け取る | オブジェクトをそのまま操作する     |
| `*job`     | 複数の位置引数をタプルで受け取る | インデックスで値を操作する         |
| `**job`    | キーワード引数を辞書で受け取る  | キー名で値を操作する               |

---

### 現在のプロジェクトでの応用例
現在のコードでは、`**job`を使って辞書をアンパックし、以下のようにキーワード引数として受け取っています。

```python
@staticmethod
def print_job_details(title, company, head_quater, categories):
    print(f"Title: {title}")
    print(f"Company: {company}")
    print(f"Headquarters: {head_quater}")
    print(f"Categories: {categories}")
    print("-" * 40)
```

この場合、`**job`で渡された辞書のキーが引数名に対応し、値がその引数に渡されます。
