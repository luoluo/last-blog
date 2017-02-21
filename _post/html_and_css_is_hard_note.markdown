---
layout: post
title: "HTML&CSS is Hard Note"
date: 2017-02-21 19:21
comments: true
categories: Wiki
---
### Basic HTML
**block-level elements:**

    <head> contains all the meatadata like page title, css stylesheet, and other things not necessarily want the user to see.
    <body> tag represents the visible content of the page.
    <title> browser display it in the page tab.
    <p>
    <h1-h6> headings are like title, but they are actually displayed on the page.
    <ul> unordered lists
    <li> list
    
        <ul>
          <li>Add a "ul" element (it stands for unordered list)</li>
          <li>Add each item in its own "li" element</li>
          <li>They don't need to be in any particular order</li>
        </ul>
    
    <ol> ordered list

**inline elements:**

    <em> italic
    <strong> blod

HTML vs CSS (structure versus presentation)
HTML markup should provide sematic information about your content-not presentation infomation

**css hierarchy for every web page:**

1. The browser's default stylesheet
2. User defined stylesheet
3. External stylesheet
4. Page-specific stylesheet
5. Inline styles

### CSS box model:

1. **Block boxes** always appear **below** the previous block element.
2. The **width of block boxes** is set automatically based on the width of its parent container.
3. The default **height of block boxes** is based on the content it contains.
4. **Inline boxes** don't affect **vertical spacing**.
5. The **width of inline boxes** is based on the contents it contains, not the width of the parent container.

**box properties:**

1. Content: The text, image or other media in the element.
2. Padding: The space between box's content and its border.
3. Border: The line between box's margin and padding.
4. Margin: The space between the box and surrounding boxes.

css example:

    padding: 50px;  /* each side 50px */
    padding: 10px 20px;  /* Vertical Horizontal */
    padding: 10px 20px 10px 20px;  /* Top Right Bottom Left */
    border: 1px solid #5D6063; /* Size Style Color */

**padding vs margin:**

1. The padding of a box has color, while margins are always transparent.
2. Padding is include in the click area of an element, while margins aren't.
3. Margins collapse vertically, while padding doesn't.

**margin collapse prevent:**

1. Only consecutive elements can collapse into each other. Put an element with non-zero height between. 
2. Use padding instead.
3. Stick to top-only or bottom-only margin convention.

align box:
text-align:
block-align: auto-margin, float left/right, flexbox.

### CSS-selector

**type selector**

    body {
    }

**class selector**

    <div class="class-name" > xx </div>
    .class-name {
    }

modify class style

    <div class="class-name modify-info" > xx </div>
    .class-name {
    }
    .modify-info {
    }

**id selector**

    <div id="bottom1"> xx </div>
    #bottom1 {
    }

### Float

    float: left; /* left align */
    float: right; /* right align */
    float: none; /* default align */
    margin: 0 auto; /* center align */

Float multiple elements in the same direction, they will stack horizontally.
By default, the height of our floated elements don't contribute to the vertical position of the footer,
so it simply sticks to itself below the last element that was not *floated*.

**clearing float:**

    .footer {
        clear: both; /* clear left/right/both */
    }

**hidden overflow:**

    .content {
        overflow: hidden;
    }

To summarize, when you have an extra unfloated HTML element at the bottom of a container div, use the clear 
solution. Otherwise, add an overflow: hidden declaration to the container element. 

### Flexbox

*horizontal align: justify-content*   
*vertical align: align-item*   

    .container {
        /* ... */
        display: flex;
        justify-content: cneter; /* center/flex-start/flex-end/space-around/space-between */
        align-item: center; /* center/flex-start(top)/flex-end(bottom)/stretch/baseline */
        flex-wrap: wrap; /* wrap/nowrap */
        flex-direction: row; /* row/cloumn/row-reverse/column-reverse */
    }
    .flex-item {
        order: 1; /* 1(first)/-1(last) */
        margin-left: auto;
        flex: 1; /* 1/initial */
    }

