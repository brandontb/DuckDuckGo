import requests

url = 'https://duckduckgo.com'

def test_url1():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Washington" in str(rsp_data["RelatedTopics"])

def test_url2():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Jefferson" in str(rsp_data["RelatedTopics"])

def test_url3():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Adams" in str(rsp_data["RelatedTopics"])

def test_url4():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Madison" in str(rsp_data["RelatedTopics"])

def test_url5():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Monroe" in str(rsp_data["RelatedTopics"])

def test_url6():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Jackson" in str(rsp_data["RelatedTopics"])

def test_url7():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Buren" in str(rsp_data["RelatedTopics"])

def test_url8():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Harrison" in str(rsp_data["RelatedTopics"])

def test_url9():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Tyler" in str(rsp_data["RelatedTopics"])

def test_url10():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Polk" in str(rsp_data["RelatedTopics"])

def test_url11():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Taylor" in str(rsp_data["RelatedTopics"])

def test_url12():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Fillmore" in str(rsp_data["RelatedTopics"])

def test_url13():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Pierce" in str(rsp_data["RelatedTopics"])

def test_url14():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Buchanan" in str(rsp_data["RelatedTopics"])

def test_url15():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Lincoln" in str(rsp_data["RelatedTopics"])

def test_url16():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Johnson" in str(rsp_data["RelatedTopics"])

def test_url17():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Grant" in str(rsp_data["RelatedTopics"])

def test_url18():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Hayes" in str(rsp_data["RelatedTopics"])

def test_url19():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Garfield" in str(rsp_data["RelatedTopics"])

def test_url20():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Arthur" in str(rsp_data["RelatedTopics"])

def test_url21():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Cleveland" in str(rsp_data["RelatedTopics"])

def test_url22():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Harrison" in str(rsp_data["RelatedTopics"])

def test_url23():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "McKinley" in str(rsp_data["RelatedTopics"])

def test_url24():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Roosevelt" in str(rsp_data["RelatedTopics"])

def test_url25():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Taft" in str(rsp_data["RelatedTopics"])

def test_url26():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Wilson" in str(rsp_data["RelatedTopics"])

def test_url27():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Harding" in str(rsp_data["RelatedTopics"])

def test_url28():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "" in str(rsp_data["RelatedTopics"])

def test_url29():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Coolidge" in str(rsp_data["RelatedTopics"])

def test_url30():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Hoover" in str(rsp_data["RelatedTopics"])

def test_url31():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Truman" in str(rsp_data["RelatedTopics"])

def test_url32():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Eisenhower" in str(rsp_data["RelatedTopics"])

def test_url33():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Kennedy" in str(rsp_data["RelatedTopics"])

def test_url34():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Johnson" in str(rsp_data["RelatedTopics"])

def test_url35():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Nixon" in str(rsp_data["RelatedTopics"])

def test_url36():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Ford" in str(rsp_data["RelatedTopics"])

def test_url37():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Carter" in str(rsp_data["RelatedTopics"])

def test_url38():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Reagan" in str(rsp_data["RelatedTopics"])

def test_url39():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Bush" in str(rsp_data["RelatedTopics"])

def test_url40():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Clinton" in str(rsp_data["RelatedTopics"])

def test_url41():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Obama" in str(rsp_data["RelatedTopics"])

def test_url42():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Trump" in str(rsp_data["RelatedTopics"])

def test_url43():
    resp = requests.get(url + '/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Biden" in str(rsp_data["RelatedTopics"])

