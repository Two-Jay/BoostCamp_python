from email.quoprimime import quote
from urllib.request import urlopen
import os
import csv
import asyncio

async def request_command_data(file_path: str):
    url = "https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/command_data.csv"
    os.system(f"curl -o {file_path} {url}")

def read_command_data(file_path: str):
    command_data = []
    with open(file_path, "r") as f:
        spamreader = csv.reader(f, delimiter=",", quotechar='"')
        for line in spamreader:
            command_data.append(line)
    return command_data

def make_dict_command_by_count(command_data: list):
    command_data_dict = {}
    for data in command_data:
        if data[1] in command_data_dict.keys():
            command_data_dict[data[1]] += 1
        else:
            command_data_dict[data[1]] = 1
    return command_data_dict

async def init_command_data():
    file_path = "/Users/kimjeongjun/BoostCamp_python/practice/command_data.csv"
    await request_command_data(file_path)
    command_data = make_dict_command_by_count(read_command_data(file_path))
    dictlist = []
    for key, value in command_data.items(): dictlist.append([key, value])
    return dictlist

def run_analyzer():
    data = asyncio.run(init_command_data())
    data.sort(key=lambda x: x[1], reverse=True)
    print(data[:100])

run_analyzer()
