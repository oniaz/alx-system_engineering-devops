# *500 Error Resolved - wp-settings.php Typo Fix*

![me when the](https://github.com/oniaz/alx-system_engineering-devops/blob/master/0x19-postmortem/images.png "me when the") <br>

**Issue Summary:**
- **Duration:** The outage lasted 41 minutes, occurring from 5:12 am to 5:33 am GMT+2.
- **Impact:** Users experienced a 500 Internal Server Error when attempting to access the webpage, resulting in an inability to access the service during the outage period.

**Root Cause:**
The root cause of the issue was identified as a typo in the `/var/www/html/wp-settings.php` file. Specifically, a file was named incorrectly as `class-wp-locale.phpp` instead of `class-wp-locale.php`.

**Timeline:**
- **5:12 am GMT+2:** The outage was discovered when users reported encountering 500 errors while attempting to access the webpage.
- **5:20 am GMT+2:** The cause of the issue was discovered through manual investigation utilizing `strace`. The investigation involved observing the Apache process ID (pid) and curling the webpage with header information (`curl -sI`). The strace command revealed a "no file or directory" error while attempting to access `class-wp-locale.phpp`.
- **5:25 am GMT+2:** A manual search confirmed the missing file and identified `class-wp-locale.php` as the correct filename. Investigative efforts focused on identifying the source of the typo, leading to the discovery of the error within the `wp-settings.php` file. The issue was isolated and addressed.
- **5:30 am GMT+2:** The typo in wp-settings.php was corrected using the sed command to replace the incorrect filename with the correct one (class-wp-locale.php).
- **5:33 am GMT+2:**  The webpage was confirmed to be functioning normally after the correction.

**Root Cause and Resolution:**
- **Root Cause Explanation:** The issue stemmed from a naming error in the `wp-settings.php` file, where a required file (`class-wp-locale.php`) was referenced with an incorrect name (`class-wp-locale.phpp`).
- **Resolution:** The problem was resolved by correcting the typo within the `wp-settings.php` file. A sed command was utilized to replace the erroneous filename with the correct one (`class-wp-locale.php`).

**Corrective and Preventative Measures:**
- **Improvements/Fixes:** Enhanced code review processes to catch naming errors and prevent similar issues in the future.
- **Specific Tasks:**
  - Implement a more thorough code review process to catch potential typos and to to ensure accuracy before deployment.
  - Implement automated tests or monitoring to detect naming inconsistencies in essential files.
  - Establish documentation standards to maintain consistency and accuracy in file naming conventions.
