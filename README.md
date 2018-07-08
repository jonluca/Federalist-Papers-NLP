# THE FEDERALIST PAPERS: AUTHOR IDENTIFICATION THROUGH K-MEANS CLUSTERING

The accompanying blog post can be found [here](https://blog.jonlu.ca/posts/the-federalist-papers-author-identification-through-k-means-clustering)

## Background

The Federalist Papers is a collection of 85 articles and essays written in the latter half of 1780 by Alexander Hamilton, James Madison, and John Jay under the pseudonym "Publius" to promote the ratification of the United States Constitution. Hamilton chose "Publius" as the pseudonym under which the series would be written - the authorship at the time of publication was a closely guarded secret. 

Following Hamilton's death in 1804, a list he wrote became public, which attributed a majority of the papers to hismelf, including some that seemed more likely the work of Madison (No. 49–58 and 62–63). The truth of who wrote the papers is still a little murky - there is general consensus on who wrote each paper, but unfortunately the truth has been lost to the annals of time. 

A significant amount of prior research has been done on the Federalist Papers, including [The Disputed Federalist Papers: SVM Feature Selection via Concave Minimization](http://pages.cs.wisc.edu/~gfung/federalist.pdf), [Case Study: The Federalist Papers](http://ptrckprry.com/course/ssd/lecture/federalist.html), and the seminal [Inference in an Authorship Problem](https://www.jstor.org/stable/2283270?seq=1#page_scan_tab_contents) by Frederick Mosteller and David L. Wallace. These papers do the topic much more justice to the subject than I can in a blog post. 

My goal is to recreate the results found by Mosteller and Wallce through modern stastical methods - namely K-Means clustering and TFIDF.