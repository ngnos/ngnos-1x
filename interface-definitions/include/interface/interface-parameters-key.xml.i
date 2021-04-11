<!-- include start from interface/interface-parameters-key.xml.i -->
<leafNode name="key">
  <properties>
    <help>Tunnel key</help>
    <valueHelp>
      <format>u32</format>
      <description>Tunnel key</description>
    </valueHelp>
    <constraint>
      <validator name="numeric" argument="--range 0-4294967295"/>
    </constraint>
    <constraintErrorMessage>key must be between 0-4294967295</constraintErrorMessage>
  </properties>
</leafNode>
<!-- include end -->