#!/usr/bin/env python3 
from GhostCrawler import main

if __name__ == '__main__':
    try:
        args = main.get_args()
        GhostCrawler = main.GhostCrawler(args)
        GhostCrawler.perform_action()
    except KeyboardInterrupt:
        print("Interrupt received! Exiting cleanly...")
