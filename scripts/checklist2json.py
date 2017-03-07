#!/usr/bin/env python3

import sys
import os
import re
import json

VERSION="0.1.0"
MULTISEL_MARKER = "<multi>"

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
    for match in re.finditer(r"^\| (?P<label>[A-Z0-9_\[\]]+)(?:\(#(?P<ref>\w+)\))? *\|( *(?P<question>[^\|\n]*) *\|)?( *(?P<answers>[^\|\n]*) *\|)?( *(?P<comment>[^\|\n]*) *\|)?",s,flags=re.M):
        answers = match.group("answers")
        answertype = "selection" # default
        if answers and MULTISEL_MARKER in answers:
            answertype = "multiselection"
            answers = answers.replace(MULTISEL_MARKER, "")
        if answers is None:
            answertype = None
        elif "/" in answers:
            answers = [a.strip() for a in answers.split("/")]
        elif "," in answers:
            answers = [a.strip() for a in answers.split(",")]
        else:
            answertype = "input"
        q = {
                "label": match.group("label").replace("[", "").replace("]", ""),
                "question": match.group("question").strip() if match.group("question") else None,
                "answers": answers,
                "answer_type": answertype,
                "comment": match.group("comment").strip() if match.group("comment") else None,
                "reference": match.group("ref"),
                }
        pos = match.start("label")
        while pos > curendpos:
            curcat = next(catiter)
            curendpos = next(endposi)
        curcat["questions"].append(q)

    catd = dict()
    for c in cats:
        catd[c["name"]] = c["questions"]

    cl = {
            "version": VERSION,
            "steps": processcats,
            "subcategories": catd,
            }
    fout.write(json.dumps(cl))

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
