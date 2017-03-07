#!/usr/bin/env python3

import sys
import os
import re


def parse(fin, fout):
    s=fin.read()
    subcatstart = re.search(r"<a name=\"cat\"",s).start()
    cats = list()
    processcats = list()
    for match in re.finditer(r"<a name=\"([A-Z0-9_]+)\"", s):
        c = {
                "name": match.group(1),
                "start": match.start(),
                "questions": list(),
            }
        cats.append(c)
        if c["start"] < subcatstart:
            processcats.append(c["name"])

    catiter = iter(cats)
    curcat = next(catiter)
    endposi = iter([ c.get("start") for c in cats ][1:] + [len(s)])
    curendpos = next(endposi)
    for match in re.finditer(r"^\| ([A-Z0-9_\[\]]+)(?:\(#\w+\))?.?\|",s,flags=re.M):
        qname = match.group(1)
        pos = match.start(1)
        while pos > curendpos:
            curcat = next(catiter)
            curendpos = next(endposi)
        curcat["questions"].append(qname)

    catd = dict()
    for c in cats:
        catd[c["name"]] = c["questions"]

    for catname in processcats:
        printcat(catd, catname, fout)

def printcat(catd, catname, fout, prefix=""):
    if prefix:
        prefix = prefix + "_"
    for q in catd[catname]:
        m = re.search("\[(\w+)\]", q)
        if not m:
            fout.write(prefix + q + "\n")
        else:
            subcatname = m.group(1)
            printcat(catd, subcatname, fout, prefix=prefix+catname)


def main():
    from optparse import OptionParser
    parser = OptionParser()
    (options, args) = parser.parse_args()

    parse(sys.stdin, sys.stdout)


if __name__ == "__main__":
    main()
