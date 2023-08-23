import pandas as pd

from input_models import Submission, KeyEvent, KeyEventType

data = pd.read_csv("/Users/andrew/Documents/keystroke-dynamics/server/accuracy_checker/train.csv")
as_dict = data.to_dict(orient="tight")

target = 'united states'
sentence_id = 0
data = []
for row in as_dict["data"]:
    username = str(row[0])
    results = row[1:]
    key_events: list[KeyEvent] = []
    for i in range(len(target)):
        key_events.append(KeyEvent(key=target[i], type=KeyEventType.KEYDOWN, timestampMillis=results[i * 2]))
        key_events.append(KeyEvent(key=target[i], type=KeyEventType.KEYUP, timestampMillis=results[i * 2 + 1]))
    ordered_key_events = sorted(key_events, key=lambda x: x["timestampMillis"])
    test_result: Submission = {"username": username, "sentenceId": sentence_id, "results": ordered_key_events}
    data.append(test_result)

even_rows = []
odd_rows = []
for i in range(len(data)):
    if i % 2 == 0:
        even_rows.append(data[i])
    else:
        odd_rows.append(data[i])

