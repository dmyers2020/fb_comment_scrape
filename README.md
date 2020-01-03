# fb_comment_scrape
getElementByClassName with .innerText to scrape comments

The wife is part of a private FB group with a very active community. A post asked about statistics related to twin births (#of weeks, weights, and time in NICU). Wanted a way to aggregate the responses. 

After some initial attmepts to use solutions available; none seemed capable of using the fb graph api to for private groups. So I hacked together a quick solution for just this one case.

A more robust solution seems fairly feasible, I'd add a step for selecting the posts first, then the related comments; and workout a quick csv creation function instead of copy-pasting. I Notice that I'm also not getting the entire text of each comment - but its late and I'm running out of interest. 
