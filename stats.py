import sqlalchemy as db
import requests
import csv
import pdb
import json
import sys
from engineStart import *

def switch(userIn):
    if userIn == 'd':
        print('downloads')
    elif userIn == 'v':
        print('views')


def getSolr():
    global record
    base_url = "https://solr.lib.umd.edu/solr/mdsoar-statistics/select?q=type%3A0+AND+bundleName%3AORIGINAL+AND+time%3A2020-01*&fl=uid%2CowningItem%2CowningComm&wt=json&indent=true&facet=true&facet.field=owningComm&rows=0"
    r = requests.get(base_url)
    jstuff = r.json()
    record = jstuff['facet_counts']['facet_fields']['owningComm']
    #do some stuff to put owningItem and owningComm in dictionary
    #can i just use the facet results? It's already tabulating for me...
    return record

def queryPGuid(commID):
    query = 'select select select'
    if len(commID) > 1:
        r = connection.execute(query,(commID,))
    else:
        r = connection.execute(query,(commID[0]))

def queryPGhandle(handle):
    query = 'select select select'

#def tabulate():
    #stuff

getSolr()
print(record)


""" engine = db.create_engine(engineStart)
connection = engine.connect()

q = '123456789/6182'
query1 = 'select text_value from metadatavalue where dspace_object_id in (select community_id from community2collection where collection_id in (select collection_id from collection2item where item_id in (select uuid from item where uuid in (select resource_id from handle where handle = %s)))) and metadata_field_id = 64'
r = connection.execute(query1,(q,))

university, = r.fetchone()
print(university) """


#for each return, take owning Comm, if owningComm has parent comm, use that, otherwise, get name of owningComm