See here formy series on Medium which dives into the data in this repository and provides more context on methodology: 

Below are the results from my testing which you may use as a template in your own testing.

Section 1: Malicious Binaries
<table><tbody><tr><th>Test description</th><th>Attack Type</th><th>Steps</th></tr><tr><td>Empire Bash stager</td><td>empire</td><td>Empire C2 Tests</td></tr><tr><td>Empire Python stager</td><td>empire</td><td>Empire C2 Tests</td></tr><tr><td>Empire deobfuscated</td><td>empire</td><td>Empire C2 Tests</td></tr><tr><td>Apfell</td><td>apfell</td><td>Apfell Tests</td></tr><tr><td>Apfell with moved osascript</td><td>apfell</td><td>Apfell Tests</td></tr><tr><td>Apfell no comments</td><td>apfell</td><td>Apfell Tests</td></tr><tr><td>Poseidon</td><td>Poseidon</td><td>Poseidon Tests</td></tr><tr><td>Poseidon obfuscation</td><td>Poseidon</td><td>Poseidon Tests</td></tr><tr><td>Poseidon UPX</td><td>Poseidon, UPX</td><td>Poseidon Tests</td></tr><tr><td>Medusa</td><td>medusa</td><td>Medusa Tests</td></tr><tr><td>Medusa obfuscation</td><td>medusa</td><td>Medusa Tests</td></tr><tr><td>Sliver</td><td>Sliver C2</td><td>Sliver Tests</td></tr></tbody></table>

Section 2: Intermediate skill TTPs for compromising endpoints: SwiftBelt, Chainbreaker
<table><tbody><tr><th>Test description</th><th>Attack Type</th><th>Steps</th></tr><tr><td>Chainbreaker</td><td>Chainbreaker</td><td>Chainbreaker Tests</td></tr><tr><td>Swiftbelt</td><td>SwiftBelt</td><td>Swiftbelt Tests</td></tr></tbody></table>

Section 3: Intermediate skill TTPs for compromising endpoints: Shells
<table><tbody><tr><th>Test description</th><th>Attack Type</th><th>Steps</th></tr><tr><td>Microsoft Word Shell via Macro</td><td>EvilOSX, MacroGenerator</td><td>Microsoft Word Shell via Macro</td></tr><tr><td>EvilOSX Test</td><td>EvilOSX</td><td>EvilOSX Test</td></tr><tr><td>Microsoft Excel Netcat Listener via Macro</td><td>Netcat</td><td>Microsoft Excel Netcat Listener via Macro</td></tr><tr><td>Msfvenom Reverse TCP</td><td>Msfvenom</td><td>Msfvenom Reverse TCP</td></tr><tr><td>Socat</td><td>Socat</td><td>Socat</td></tr><tr><td>Netcat</td><td>Netcat</td><td>Netcat</td></tr><tr><td>PTY</td><td>PTY module</td><td>PTY</td></tr></tbody></table>

Section 4: Process Injection
<table><tbody><tr><th>Test description</th><th>Attack Type</th><th>Steps</th></tr><tr><td>Visual Studio Code Process Injection</td><td>Electron process injection</td><td>Visual Studio Code Process Injection</td></tr><tr><td>Visual Studio Code Process Injection Persistence</td><td>Electron process injection</td><td>Visual Studio Code Process Injection Persistence</td></tr></tbody></table>

Section 5: PUP Detections
<table><tbody><tr><th>Test description</th><th>Attack Type</th><th>Steps</th></tr><tr><td>TOR</td><td>TOR</td><td>TOR</td></tr><tr><td>Mouse Jiggler</td><td>Jolt of Caffeine</td><td>Jolt of Caffeine</td></tr><tr><td>Keylogger</td><td>keylogger</td><td>Keylogger</td></tr><tr><td>Keylogger Persistence Test</td><td>keylogger</td><td>Keylogger Persistence Test</td></tr></tbody></table>

Section 6: Attempt to disable the agent or file shipper
<table><tbody><tr><th>Test description</th><th>Attack Type</th><th>Steps</th></tr><tr><td>Add entry to etc/hosts</td><td>etc/hosts entry</td><td>Add entry to etc hosts</td></tr><tr><td>Attempt to uninstall</td><td>uninstall</td><td>Attempt to uninstall</td></tr><tr><td>Attempt to kill processes</td><td>pkill</td><td>Attempt to kill processes</td></tr></tbody></table>

Section 7: Testing whether Enterprise YARA Solution can collect new file types
<table><tbody><tr><th>Test description</th><th>Attack Type</th><th>Steps</th></tr><tr><td>.gif</td><td>Downloaded a .gif</td><td>Testing whether Enterprise YARA Solution can collect new file types</td></tr><tr><td>.ova</td><td>Downloaded a .ova</td><td>Testing whether Enterprise YARA Solution can collect new file types</td></tr><tr><td>.rtf</td><td>Created a .rtf</td><td>Testing whether Enterprise YARA Solution can collect new file types</td></tr></tbody></table>

Section 8: Import YARA Rules from other reputable intel sources into Enterprise YARA Solution
<table><tbody><tr><th>Test description</th><th>Attack Type</th><th>Steps</th></tr><tr><td>Usage of paid and open source intel</td><td>Paid: Crowdstrike / Free: Florian Roth, Reversing Labs, Elastic Security, ESET Research, Chronicle, Strangereal Intel, Blackorbird</td><td>Import YARA Rules from other reputable intel sources into Enterprise YARA Solution</td></tr></tbody></table>

Detection Results Summary
<table><tbody><tr><th>Detetion Result</th><th>EDR Solution 1</th><th>EDR Solution 2</th><th>YARA Solution</th></tr><tr><td>Detected and Blocked</td><td>10</td><td>12</td><td>N/A</td></tr><tr><td>Detected Only</td><td>0</td><td>2</td><td>11</td></tr></tbody></table>
