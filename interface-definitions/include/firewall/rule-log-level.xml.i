<!-- include start from firewall/common-rule.xml.i -->
<leafNode name="log">
  <properties>
    <help>Option to log packets matching rule</help>
    <completionHelp>
      <list>emerg alert crit err warn notice info debug</list>
    </completionHelp>
    <valueHelp>
      <format>emerg</format>
      <description>Emerg log level</description>
    </valueHelp>
    <valueHelp>
      <format>alert</format>
      <description>Alert log level</description>
    </valueHelp>
    <valueHelp>
      <format>crit</format>
      <description>Critical log level</description>
    </valueHelp>
    <valueHelp>
      <format>err</format>
      <description>Error log level</description>
    </valueHelp>
    <valueHelp>
      <format>warn</format>
      <description>Warning log level</description>
    </valueHelp>
    <valueHelp>
      <format>notice</format>
      <description>Notice log level</description>
    </valueHelp>
    <valueHelp>
      <format>info</format>
      <description>Info log level</description>
    </valueHelp>
    <valueHelp>
      <format>debug</format>
      <description>Debug log level</description>
    </valueHelp>
    <constraint>
      <regex>(emerg|alert|crit|err|warn|notice|info|debug)</regex>
    </constraint>
  </properties>
</leafNode>
<!-- include end -->