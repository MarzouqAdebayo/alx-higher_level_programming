# 0x15. JavaScript - Web jQuery

Front-endJavaScript

#### Question #0

In the following code snippet, does the selector called `('header.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class="my_header"&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #1

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header id="my_header"&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #2

How many HTML tags are present in the following HTML code?

-   `<!DOCTYPE html>` is not an HTML tag
-   `<head></head>` is considered one HTML tag.

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   4
    
-   7
    
-   6
    
-   5
    

#### Question #3

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class="my_header"&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #4

In the following code snippet, does the selector called `('.header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #5

In the following code snippet, does the selector called `('body header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #6

How many HTML tags are present in the following HTML code?

-   `<!DOCTYPE html>` is not an HTML tag
-   `<head></head>` is considered one HTML tag.

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   11
    
-   14
    
-   13
    
-   12
    

#### Question #7

In the following code snippet, does the selector called `('HeAdER')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Tips:

Selectors are case insensitive

#### Question #8

In the following code snippet, does the selector called `('header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #9

How many HTML tags are present in the following HTML code?

-   `<!DOCTYPE html>` is not an HTML tag
-   `<head></head>` is considered one HTML tag.

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   15
    
-   20
    
-   18
    
-   16
    

#### Question #10

In the following code snippet, does the selector called `('.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class="my_header"&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #11

In the following code snippet, does the selector called `('section.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class="my_header"&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #12

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class="my_header"&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul id="my_header"&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

#### Question #13

In the following code snippet, does the selector called `('#header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles/global.css" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;section&gt;
      &lt;img src="logo.jpg" alt="" /&gt;
      &lt;br /&gt;
      &lt;ul&gt;
        &lt;li&gt;Home&lt;/li&gt;
        &lt;li&gt;Admission &lt;span class="btn"&gt;apply&lt;/span&gt;&lt;/li&gt;
        &lt;li&gt;Login&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/section&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
```

-   Yes
    
-   No
    

## Tasks

### 0\. No JQuery

mandatory

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

-   You must use `document.querySelector` to select the HTML tag
-   You can’t use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 0-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="0-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `0-script.js`

Done?!

### 1\. With JQuery

mandatory

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 1-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="1-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `1-script.js`

Done?!

### 2\. Click and turn red

mandatory

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 2-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id="red_header"&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="2-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `2-script.js`

Done?!

### 3\. Add \`.red\` class

mandatory

Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`

-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 3-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id="red_header"&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="3-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `3-script.js`

Done?!

### 4\. Toggle classes

mandatory

Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:

-   The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
-   If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 4-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class="green"&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id="toggle_header"&gt;Toggle header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="4-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `4-script.js`

Done?!

### 5\. List of elements

mandatory

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

-   The new element must be: `<li>Item</li>`
-   The new element must be added to `UL.my_list`
-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 5-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="add_item"&gt;Add item&lt;/div&gt;
    &lt;br /&gt;
    &lt;ul class="my_list"&gt;
      &lt;li&gt;Item&lt;/li&gt;
    &lt;/ul&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="5-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `5-script.js`

Done?!

### 6\. Change the text

mandatory

Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`

-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 6-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="update_header"&gt;Update the header&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="6-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `6-script.js`

Done?!

### 7\. Star wars character

mandatory

Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`

-   The name must be displayed in the HTML tag `DIV#character`
-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 7-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars character
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="character"&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="7-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `7-script.js`

Done?!

### 8\. Star Wars movies

mandatory

Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`

-   All movie titles must be list in the HTML tag `UL#list_movies`
-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 8-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars movies
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;ul id="list_movies"&gt;
    &lt;/ul&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="8-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `8-script.js`

Done?!

### 9\. Say Hello!

mandatory

Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.

-   The translation of “hello” must be displayed in the HTML tag `DIV#hello`
-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API
-   Your script must work when it is imported from the `<head>` tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 9-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="9-script.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Say Hello!
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="hello"&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `9-script.js`

Done?!

### 10\. No jQuery - document loaded

#advanced

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

-   You must use `document.querySelector` to select the HTML tag
-   You can’t use the jQuery API
-   Note: Your script must be imported from the `<head>` tag, not at the end of the HTML

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 100-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script type="text/javascript" src="100-script.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `100-script.js`

Done?!

### 11\. List, add, remove

#advanced

Write a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks:

-   The new element must be: `<li>Item</li>`
-   The new element must be added to `UL.my_list`
-   When the user clicks on `DIV#add_item`: a new element is added to the list
-   When the user clicks on `DIV#remove_item`: the last element is removed from the list
-   When the user clicks on `DIV#clear_list`: all elements of the list are removed
-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API
-   You script must work when it imported from the `HEAD` tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 101-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="101-script.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="add_item"&gt;Add item&lt;/div&gt;
    &lt;div id="remove_item"&gt;Remove item&lt;/div&gt;
    &lt;div id="clear_list"&gt;Clear list&lt;/div&gt;
    &lt;br /&gt;
    &lt;ul class="my_list"&gt;
      &lt;li&gt;Item&lt;/li&gt;
    &lt;/ul&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `101-script.js`

Done?!

### 12\. Say hello to everybody!

#advanced

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

-   You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
-   The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
-   The translation must be fetched when the user clicks on `INPUT#btn_translate`
-   The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API
-   You script must work when imported from the `<head>` tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 102-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="102-script.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Say Hello
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;input id="language_code" type="text" placeholder="Language code"/&gt;
    &lt;input id="btn_translate" type="button" value="Translate"/&gt;
    &lt;br /&gt;
    &lt;div id="hello"&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `102-script.js`

Done?!

### 13\. And press ENTER

#advanced

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

-   You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
-   The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
-   The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
-   The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
-   You can’t use `document.querySelector` to select the HTML tag
-   You must use the JQuery API
-   You script must work when imported from the `<head>` tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 103-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="103-script.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Say Hello
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;input id="language_code" type="text" placeholder="Language code"/&gt;
    &lt;input id="btn_translate" type="button" value="Translate"/&gt;
    &lt;br /&gt;
    &lt;div id="hello"&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x15-javascript-web_jquery`
-   File: `103-script.js`
