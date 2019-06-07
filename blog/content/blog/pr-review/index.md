---
title: How I review PRs
date: "2019-06-06"
description: 1 words
---1. Reason about potential bugs that could be in the code (as a more experienced developer you may catch some)

1. Find structural issues with code (bad abstractions)

1. Find clarity / readability issues (overly long functions, bad variable names)

1. Code style issues. In general these should be automated by a linter (prettier in javascript, for instance)

In a given review I find it most effective to stick to one level. Iterate until all concerns at that level are addressed.
Iteration time / priority allowing, move at most one more level deep. Iterating through all four levels should be avoided unless the reviewee is a highly experienced developer who's adapting to the team's conventions. 

