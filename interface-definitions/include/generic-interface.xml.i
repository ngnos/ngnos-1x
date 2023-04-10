<!-- include start from generic-interface.xml.i -->
<leafNode name="interface">
  <properties>
    <help>Interface to use</help>
    <completionHelp>
      <script>${ngnos_completion_dir}/list_interfaces</script>
    </completionHelp>
    <valueHelp>
      <format>txt</format>
      <description>Interface name</description>
    </valueHelp>
    <constraint>
      #include <include/constraint/interface-name.xml.i>
    </constraint>
  </properties>
</leafNode>
<!-- include end -->
