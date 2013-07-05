Title: Wordpress 3.5 and Broken Eclipse Theme 
Date: 2013-01-20 
Tags: wordpress, php
Slug: wordpress35-eclipse 

There are a couple of wordpress sites that I maintain. The nice thing about wordpress is that most of the time it is pretty easy to maintain and manage upgrades. The key is “most" of the time. I purchased a custom theme for a website that I manage called Eclipse. Unfortunately it does not seem to be maintained any longer and when I upgraded the site to wordpress 3.5, it broke. Word for the wise, backup your wordpress database before a seemingly minor upgrade. Yes, I know I should have done a backup. The Eclipse theme breaks when trying to use the Attachments plugin. Even if you upgrade the plugin, the theme is still broken. I did find a quick way to fix the problem. Just wrap the call for the attachments plugin in page.php and single.php with the following function:

```php
if (function_exists('function_name')) { 
  function_name() 
}
```
This will then check for the plugin before trying to run the code. This is not a perfect fix, but has bought me a bit of time until I troubleshoot the root problem. I thought it may be a useful bit of information for someone like me, a non-php guy (python guy) who happens to manage a couple of small sites with wordpress.
