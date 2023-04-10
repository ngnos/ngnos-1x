<!-- include start from firewall/match-interface.xml.i -->
<leafNode name="interface-name">
  <properties>
    <help>Match interface</help>
    <completionHelp>
      <script>${ngnos_completion_dir}/list_interfaces</script>
    </completionHelp>
  </properties>
</leafNode>
<leafNode name="interface-group">
  <properties>
    <help>Match interface-group</help>
    <completionHelp>
      <path>firewall group interface-group</path>
    </completionHelp>
  </properties>
</leafNode>
<!-- include end -->
