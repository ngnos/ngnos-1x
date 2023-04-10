<!-- include start from ip-protocol.xml.i -->
<leafNode name="protocol">
    <properties>
      <help>Protocol</help>
      <valueHelp>
        <format>txt</format>
        <description>Protocol name</description>
      </valueHelp>
      <completionHelp>
        <script>${ngnos_completion_dir}/list_protocols.sh</script>
      </completionHelp>
      <constraint>
        <validator name="ip-protocol"/>
      </constraint>
    </properties>
</leafNode>
<!-- include end from ip-protocol.xml.i -->
