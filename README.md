# CS515-prj1

## Author
- Name: Wai Hou Cheang
- Stevens Login: wcheang@stevens.edu
- GitHub Repo URL: https://github.com/s-inu/CS515-prj1

## Time Spent
- Estimated hours spent on the project: 14 hrs

## Testing
- Description of how the code was tested:
  - create some example files, and manually run and compare them
  

## Known Bugs and Issues
- N/A

## Difficult Issues and Resolutions
- wc
  - no-args means every args is True
    - made control flow in main()

- different source, from args or STDIN
  - make default as `stdin`

## Implemented Extensions
1. **Extension 1**: wc-multiple files
   - How to test:
     - Windows
       -  `python wc.py foo bar`
2. **Extension 2**: wc-flags to control output
   - How to test: 
     - Windows
       - `python wc.py foo bar -l`
       - `python wc.py -lw foo bar ` 
3. **Extension 3**: gron-control the base-object name
   - How to test: 
     - Windows
       - `python gron.py eg.json | grep kwds | python ungron.py `

